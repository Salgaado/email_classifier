const toggleBtn = document.getElementById('theme-toggle');
const body = document.body;

const saved = localStorage.getItem('theme') || 'light';
body.classList.toggle('dark-theme', saved === 'dark');
toggleBtn.textContent = saved === 'dark' ? '🌙' : '☀️';
toggleBtn.addEventListener('click', () => {

  const isDark = body.classList.toggle('dark-theme');
  toggleBtn.textContent = isDark ? '🌙' : '☀️';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

const form = document.getElementById('email-form');
const fileInput = document.getElementById('file-input');
const textoInputEl = document.getElementById('texto');
const removeButton = document.getElementById('remove-file');
const spinner = document.getElementById('spinner');

fileInput.addEventListener('change', () => {
  if (fileInput.files.length > 0) {
    textoInputEl.disabled = true;
    removeButton.hidden = false;
  } else {
    textoInputEl.disabled = false;
    removeButton.hidden = true;
  }
});

removeButton.addEventListener('click', () => {
  fileInput.value = '';
  textoInputEl.disabled = false;
  removeButton.hidden = true;
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const textoInput = textoInputEl.value.trim();
  const formData = new FormData();
  if (fileInput.files.length) {
    formData.append('file', fileInput.files[0]);
  } else if (textoInput) {
    formData.append('texto', textoInput);
  } else {
    return alert('Insira texto ou faça upload de um arquivo .txt ou .pdf');
  }
  spinner.style.display = 'block';

  document.getElementById('categoria').textContent = 'Processando…';
  document.getElementById('resposta').textContent = '';
  document.getElementById('resultado').classList.remove('hidden');

  try {
    const res = await fetch('https://email-classifier-2-9xp8.onrender.com/processar', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error);

    document.getElementById('categoria').textContent = data.categoria;
    document.getElementById('resposta').textContent = data.resposta;
  } catch (err) {
    document.getElementById('categoria').textContent = 'Erro';
    document.getElementById('resposta').textContent = err.message;
  }finally {
    spinner.style.display = 'none';
  }
});
