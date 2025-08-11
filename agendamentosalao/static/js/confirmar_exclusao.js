document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".btn-delete").forEach(function(button) {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            let url = this.getAttribute("data-url");

            Swal.fire({
                title: "Tem certeza?",
                text: "Essa ação não poderá ser desfeita!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#d33",
                cancelButtonColor: "#3085d6",
                confirmButtonText: "Sim, excluir",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = url;
                }
            });
        });
    });
});
