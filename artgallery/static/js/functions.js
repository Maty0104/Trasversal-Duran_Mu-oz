const form =document.querySelector('#form')

const nombre = form.nombre
const apellidopaterno = form.apeP
const apellidomaterno =form.apeM
const genero = form.sexo
const rut= form.rut
const dirección=form.dirección
const correo=form.correo
const teléfono=form.teléfono
const terminos=form.terminos

let errors = document.querySelector('#errors')

form.addEventListener('submit', validar)

function validar(e){
    errors.innerHTML=''
    validarNombres(e)
    validarApellidopaterno(e)
    validarApellidomaterno(e)
    validarGenero(e)
    validarRut(e)
    validarDirección(e)
    validarCorreo(e)
    validarTeléfono(e)
    validarTerminos(e)
}


function validarNombres(e){
    if (nombre.value== '' || nombre.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Nombres</li>'
        e.preventDefault()
    }
}

function validarApellidopaterno(e){
    if (apellidopaterno.value== '' || apellidopaterno.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Apellido Paternos</li>'
        e.preventDefault()
    }
}

function validarApellidomaterno(e){
    if (apellidomaterno.value== '' || apellidomaterno.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Apellido Maternos</li>'
        e.preventDefault()
    }
}

function validarGenero(e){
if (sexo[0].checked == false  && sexo[1].checked == 
    false){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Seleccione sexo</li>'
        e.preventDefault()}    
}

function validarRut(e){
    if (rut.value== '' || rut.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Rut</li>'
        e.preventDefault()
    }
}

function validarDirección(e){
    if (dirección.value== '' || dirección.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Direccion</li>'
        e.preventDefault()
    }
}

function validarCorreo(e){
    if (correo.value== '' || correo.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Correo</li>'
        e.preventDefault()
    }else{
        if(/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(correo.value)){ 

        }else {
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Correo</li>'
        e.preventDefault()

        }
    }

}
function validarTeléfono(e){
    if (teléfono.value== '' || teléfono.value == null){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Ingrese Telefono</li>'
        e.preventDefault()
    }
}
function validarTerminos(e){
    if (!terminos.checked){
        errors.styles.display = 'block'
        errors.innerHTML += '<li>Acepte terminos</li>'
        e.preventDefault()
    }
}