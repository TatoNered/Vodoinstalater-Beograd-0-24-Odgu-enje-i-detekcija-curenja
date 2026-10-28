/* Minimalna logika: označavanje aktivne stavke i meko slanje forme. */
(function () {
  "use strict";

  // Forma za upit — bez bekenda samo pokazuje poruku.
  var forms = document.querySelectorAll("form[data-quote]");
  Array.prototype.forEach.call(forms, function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = f.querySelector("[data-ok]");
      if (ok) {
        ok.hidden = false;
        ok.setAttribute("role", "status");
      }
      f.reset();
    });
  });
})();
