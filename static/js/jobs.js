const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editButtons = document.getElementsByClassName("btn-edit");
const editForm = document.getElementById("editForm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        editModal.show()
        let jobId = e.target.getAttribute("data-job_id");
        editForm.setAttribute("action", `history/update/${jobId}`);
    });
}
