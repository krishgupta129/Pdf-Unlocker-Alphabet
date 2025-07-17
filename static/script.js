const form = document.getElementById('unlockForm');
const currentSpan = document.getElementById('current');
const foundSpan = document.getElementById('found');
const downloadBtn = document.getElementById('downloadBtn');
let statusInterval;

form.onsubmit = async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const charset = form.charset.value;
  formData.append('charset', charset);

  downloadBtn.classList.remove('active');
  await fetch('/start', { method: 'POST', body: formData });
  startStatusUpdates();
};

function pause() {
  fetch('/pause');
}

function resume() {
  fetch('/resume');
}

function stop() {
  fetch('/stop');
  clearInterval(statusInterval);
}

function startStatusUpdates() {
  statusInterval = setInterval(async () => {
    const res = await fetch('/status');
    const data = await res.json();
    currentSpan.textContent = data.current_try;
    foundSpan.textContent = data.found_password;

    if (data.unlocked) {
      downloadBtn.classList.add('active');
      clearInterval(statusInterval);
    }
  }, 200);
}
