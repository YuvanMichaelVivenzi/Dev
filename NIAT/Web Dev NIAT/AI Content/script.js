// This is AI-generated content.

// Add pizzazz: button animation, confetti, and color mode toggle

document.addEventListener('DOMContentLoaded', function() {
  // Button animation
  const button = document.querySelector('button');
  if (button) {
    button.addEventListener('mouseenter', () => {
      button.style.transform = 'scale(1.1) rotate(-3deg)';
      button.style.boxShadow = '0 4px 20px 0 rgba(0,0,0,0.2)';
    });
    button.addEventListener('mouseleave', () => {
      button.style.transform = '';
      button.style.boxShadow = '';
    });
    button.addEventListener('click', () => {
      launchConfetti();
    });
  }

  // Color mode toggle
  const modeBtn = document.createElement('button');
  modeBtn.textContent = '🌙 Toggle Dark Mode';
  modeBtn.className = 'mode-toggle';
  document.body.insertBefore(modeBtn, document.body.firstChild);
  modeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    modeBtn.textContent = document.body.classList.contains('dark-mode') ? '☀️ Toggle Light Mode' : '🌙 Toggle Dark Mode';
  });
});

// Simple confetti effect
function launchConfetti() {
  for (let i = 0; i < 30; i++) {
    const conf = document.createElement('div');
    conf.className = 'confetti';
    conf.style.left = Math.random() * 100 + 'vw';
    conf.style.background = `hsl(${Math.random()*360}, 80%, 60%)`;
    conf.style.animationDuration = (Math.random() * 1 + 1.5) + 's';
    document.body.appendChild(conf);
    setTimeout(() => conf.remove(), 2000);
  }
}
