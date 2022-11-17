const buttonDelete = document.querySelectorAll('.btn-delete');
if (buttonDelete){
    // creo un array con los botones que contiene esa clase
    const arrayButtons = Array.from(buttonDelete);
    arrayButtons.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{
            console.log(e)
            if(!confirm("Seguro que desea eliminar?")){
                e.preventDefault();
            }
        })
    })
}
