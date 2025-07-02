document.addEventListener("DOMContentLoaded", function () {
    const input = document.querySelector('input[type="file"][name="image"]');
    const preview = document.getElementById("preview-image");

    if (input && preview) {
        input.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
              function previewImage(event) {
    const preview = document.getElementById('preview-img');
    const file = event.target.files[0];

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = 'block';

        // Optionally hide current profile image
        const oldPreview = document.getElementById('preview-image');
        if (oldPreview) {
            oldPreview.style.opacity = 0.4;
        }
    }
}
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
