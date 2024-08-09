document.addEventListener('DOMContentLoaded', () => {
    console.log('Documento cargado yiiiiiii');
    const formulario = document.querySelector('.contenedor-formulario');
    const fechaNacimiento = document.getElementById('fecha_nacimiento');

    formulario.addEventListener('submit', (e) => {
        const fechaActual = new Date();
        const fechaSeleccionada = new Date(fechaNacimiento.value);

        console.log('Fecha actual:', fechaActual);
        console.log('Fecha seleccionada:', fechaSeleccionada);

        if (fechaSeleccionada > fechaActual) {
            e.preventDefault();
            alert('A mi no me mamas, la fecha que pusiste no ha pasado todavia >:D');
        }

        const contraseña = document.getElementById('contraseña');
        const confirmarContraseña = document.getElementById('confirmar-contraseña');
        if (confirmarContraseña.value !== contraseña.value) {
            e.preventDefault();
            alert('Las contraseñas no coinciden');
        }
    });
});