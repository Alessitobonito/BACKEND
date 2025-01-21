const btnCrearProducto = document.getElementById('btnCrearProducto');
const nombreProducto = document.getElementById('nombreProducto');
const descripcionProducto = document.getElementById('descripcionProducto');
btnCrearProducto.addEventListener('click', e=>{
    if(nombreProducto.value === '' || descripcionProducto.value === ''){
        alert('Debes rellenar todos los campos');
        e.preventDefault(); 
    }

});