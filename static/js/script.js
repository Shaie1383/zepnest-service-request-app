document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".js-confirm-delete").forEach((button) => {
        button.addEventListener("click", (event) => {
            if (!window.confirm("Delete this service request? This action cannot be undone.")) {
                event.preventDefault();
            }
        });
    });

    window.setTimeout(() => {
        document.querySelectorAll(".alert").forEach((alertElement) => {
            const bootstrapAlert = bootstrap.Alert.getOrCreateInstance(alertElement);
            bootstrapAlert.close();
        });
    }, 5000);
});
