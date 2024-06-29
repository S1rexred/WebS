    function togglePopup() {
      var popup = document.getElementById("popup");
      if (popup.style.display === "none") {
        popup.style.display = "block";
        document.addEventListener("click", closePopupOutside);
      } else {
        popup.style.display = "none";
        document.removeEventListener("click", closePopupOutside);
      }
    }

    function closePopupOutside(event) {
      var popup = document.getElementById("popup");
      if (!popup.contains(event.target)) {
        popup.style.display = "none";
        document.removeEventListener("click", closePopupOutside);
      }
    }
  