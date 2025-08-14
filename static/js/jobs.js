const editModal = new bootstrap.Modal(document.getElementById("editModal"));
const editButtons = document.getElementsByClassName("btn-edit");
const editForm = document.getElementById("editForm");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        editModal.show()
        let jobId = e.target.getAttribute("data-job_id");
        editForm.setAttribute("action", `history/update/${jobId}`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) =>{
        deleteModal.show()
        let jobId = e.target.getAttribute("data-job_id");
        deleteConfirm.href = `history/delete/${jobId}`
    });
}
