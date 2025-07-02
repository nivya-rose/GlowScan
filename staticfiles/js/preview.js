document.addEventListener("DOMContentLoaded", function () {
    const input = document.querySelector('input[type="file"][name="image"]');
    const preview = document.getElementById("preview-image");

    if (input && preview) {
        input.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    preview.src = e.target.result;
                    preview.style.display = "block";
                };
                reader.readAsDataURL(file);
            }
        });
    }
});
