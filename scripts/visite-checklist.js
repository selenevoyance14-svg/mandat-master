(() => {
  'use strict';
  const tool = document.getElementById('visit-tool');
  if (!tool) return;
  const tasks = Array.from(tool.querySelectorAll('[data-task]'));
  const reference = document.getElementById('visit-reference');
  const notice = document.getElementById('visit-notice');
  const progress = document.getElementById('visit-progress');
  const status = document.getElementById('visit-progress-text');
  const download = document.getElementById('visit-download');
  const reset = document.getElementById('visit-reset');
  const print = document.getElementById('visit-print');
  function update() {
    const completed = tasks.filter(task => task.checked).length;
    progress.value = completed;
    status.textContent = `${completed} sur ${tasks.length} points cochés${completed === tasks.length ? ' — liste complétée' : ''}`;
    notice.textContent = '';
  }
  tasks.forEach(task => task.addEventListener('change', update));
  [download, reset, print].forEach(button => { button.hidden = false; });
  reset.addEventListener('click', () => {
    tasks.forEach(task => { task.checked = false; });
    reference.value = '';
    update();
    notice.textContent = 'La checklist et sa référence ont été remises à zéro. Un fichier déjà téléchargé reste sur votre appareil.';
  });
  download.addEventListener('click', () => {
    const lines = ['CHECKLIST DE VISITE — MandatMaster', `Référence interne : ${reference.value.trim() || 'Non renseignée'}`, '', status.textContent, ''];
    tool.querySelectorAll('fieldset').forEach(group => {
      lines.push(group.querySelector('legend').textContent, '');
      group.querySelectorAll('label').forEach(label => lines.push(`[${label.querySelector('input').checked ? 'x' : ' '}] ${label.querySelector('span').textContent}`));
      lines.push('');
    });
    lines.push('Support d’organisation à adapter aux consignes de votre structure.', 'https://mandatmaster.fr/checklist-visite');
    const url = URL.createObjectURL(new Blob(['\uFEFF', lines.join('\n')], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'checklist-visite-mandatmaster.txt';
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    notice.textContent = 'Votre checklist a été préparée pour le téléchargement. Vérifiez le dossier de téléchargements de votre navigateur.';
  });
  print.addEventListener('click', () => window.print());
  update();
})();
