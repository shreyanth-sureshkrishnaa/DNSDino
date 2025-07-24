document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("darkModeToggle");
    const logo = document.getElementById("logo");
    const favicon = document.getElementById("favicon");

   
    function applyDarkMode(isDark) {
        document.body.classList.toggle("dark-mode", isDark);
        localStorage.setItem("dark-mode", isDark);

        if (logo) {
            logo.src = isDark
                ? "/static/logo-dark.svg"
                : "/static/logo-light.svg";
        }

        if (favicon) {
            favicon.href = isDark
                ? "/static/logo-dark.svg"
                : "/static/logo-light.svg";
        }
    }


    const savedMode = localStorage.getItem("dark-mode") === "true";
    applyDarkMode(savedMode);

    if (toggle) {
        toggle.checked = savedMode;

        toggle.addEventListener("change", function () {
            applyDarkMode(toggle.checked);
        });
    }
});
