//script for mobile nev sidebar
  const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("overlay");

    function openMenu() {
      sidebar.classList.remove("translate-x-full");
      overlay.classList.remove("opacity-0", "pointer-events-none");
    }

    function closeMenu() {
      sidebar.classList.add("translate-x-full");
      overlay.classList.add("opacity-0", "pointer-events-none");
    }