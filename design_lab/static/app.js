const byId = (id) => document.getElementById(id);
let current = null;
let busy = false;

function status(message, error = false) {
  byId('status').textContent = message;
  byId('status').classList.toggle('error', error);
}
function lock(value) {
  busy = value;
  byId('generate').disabled = value;
  document.querySelectorAll('[data-choice]').forEach((button) => {
    button.disabled = value || Boolean(current?.preference);
  });
  byId('reason').disabled = value || Boolean(current?.preference);
}
async function request(path, body) {
  const options = body ? {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)} : {};
  const response = await fetch(path, options);
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || 'The request could not be completed.');
  return data;
}
function show(record) {
  current = record;
  byId('empty').hidden = true;
  byId('results').hidden = false;
  ['left', 'right'].forEach((side, index) => {
    byId(`${side}-image`).src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(record.designs[index].svg);
    byId(`${side}-image`).alt = `${side} poster: ${record.brief.title}. ${record.brief.details}. ${record.brief.cta}`;
  });
  for (const key of ['title', 'details', 'cta']) byId(key).value = record.brief[key];
  byId('seed').value = record.seed;
  byId('reason').value = record.preference?.reason || '';
  byId('metrics').hidden = !record.preference;
  byId('state-label').textContent = record.preference ? 'SAVED' : 'BLIND COMPARISON';
  document.querySelectorAll('[data-choice]').forEach((button) => button.classList.toggle('selected', button.dataset.choice === record.preference?.choice));
  byId('metric-grid').replaceChildren();
  if (record.preference) {
    record.designs.forEach((design, i) => {
      const card = document.createElement('div'); card.className = 'metric-card';
      const title = document.createElement('strong'); title.textContent = i === 0 ? 'Left design' : 'Right design'; card.append(title);
      const labels = {out_of_bounds: 'Boxes outside canvas', text_box_overlaps: 'Overlapping text boxes', estimated_text_overflow: 'Estimated text overflows', minimum_contrast: 'Minimum contrast ratio'};
      for (const [key, label] of Object.entries(labels)) {
        const row = document.createElement('div'); row.className = 'metric-row';
        const name = document.createElement('span'); name.textContent = label;
        const value = document.createElement('strong'); value.textContent = design.metrics[key] + (key === 'minimum_contrast' ? ':1' : '');
        row.append(name, value); card.append(row);
      }
      byId('metric-grid').append(card);
    });
  }
  const message = record.preference ? `Preference saved: ${record.preference.choice}. Scores are now visible.` : 'Scores are hidden. Choose based on the brief and what you see.';
  status(message);
  try { localStorage.setItem('design-lab-comparison', record.id); } catch { status(message + ' Browser history is unavailable; export to retain the record ID.'); }
  lock(false);
}
byId('brief-form').addEventListener('submit', async (event) => {
  event.preventDefault(); if (busy) return;
  lock(true); status('Generating two template layouts…');
  try {
    const brief = Object.fromEntries(['title', 'details', 'cta'].map((key) => [key, byId(key).value]));
    show(await request('/api/comparisons', {brief, seed: Number(byId('seed').value)}));
  } catch (error) { status(error.message, true); lock(false); }
});
document.querySelectorAll('[data-choice]').forEach((button) => button.addEventListener('click', async () => {
  if (!current || busy || current.preference) return;
  lock(true); status('Saving your preference…');
  try { show(await request('/api/preferences', {id: current.id, choice: button.dataset.choice, reason: byId('reason').value})); }
  catch (error) { status(error.message, true); lock(false); }
}));
async function restore() {
  let id;
  try { id = localStorage.getItem('design-lab-comparison'); } catch { return; }
  if (!id) return;
  lock(true);
  try { show(await request('/api/comparisons/' + encodeURIComponent(id))); }
  catch { status('Previous comparison is unavailable. Generate a new one to begin.'); lock(false); }
}
restore();
