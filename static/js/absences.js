const editModal = new bootstrap.Modal(document.getElementById("absenceEditModal"));
const editButtons = document.getElementsByClassName("btn-absence-edit");
const editForm = document.getElementById("absenceEditForm")

const deleteButtons = document.getElementsByClassName("btn-absence-delete");


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        editModal.show()
        let absenceId = e.target.getAttribute("data-absence_id");
        editForm.setAttribute("action", `absence/edit/${absenceId}`)
    });
}