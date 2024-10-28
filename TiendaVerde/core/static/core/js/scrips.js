// Función que hace elegir las subcategorías.
document.addEventListener('DOMContentLoaded', function() {
    const selectMaterial = document.getElementById('material');
    
    // Obtengo todas las secciones de opciones.
    const opcionesMaterial = document.querySelectorAll('.material-options');
  
    // "Evento" que detecta cuando cambia la selección del material.
    selectMaterial.addEventListener('change', function() {
      // Ocultar todas las opciones.
      opcionesMaterial.forEach(function(option) {
        option.style.display = 'none';
      });
  
      // Mostrar la sección correcta basada en la selección.
      const selectedValue = selectMaterial.value;
      if (selectedValue) {
        const selectedOption = document.getElementById(selectedValue);
        if (selectedOption) {
          selectedOption.style.display = 'block';
        }
      }
    });
  });
  
  // Función que valida todos los campos del formulario.
  document.addEventListener("DOMContentLoaded", function() {
    // Obtengo las constantes por el id.
    const errorDiv    = document.getElementById("error-messages");
    const nombres     = document.getElementById("nombres");
    const correo      = document.getElementById("correo");
    const direccion   = document.getElementById("direccion");
    const cantidadRes = document.getElementById("cantidadRes");
    const material    = document.getElementById("material");
    const btnEnviar   = document.getElementById("btn-enviar");

    // Valido cuando el usuario hace clic en el botón "Enviar".
    btnEnviar.addEventListener("click", function(event) {
        event.preventDefault();  // Evitar el envío del formulario.

        let isValid = true;
        errorDiv.innerHTML = "";  // Limpiar mensajes de error previos.

        // Valido todos los campos
        if (!validateNombre()) isValid = false;
        if (!validateCorreo()) isValid = false;
        if (!validateDireccion()) isValid = false;
        if (!validateCantidad()) isValid = false;
        if (!validateMaterial()) isValid = false;

        // Si todo es válido, muestro un mensaje de éxito.
        if (isValid) {
            errorDiv.innerHTML = "<span style='color: green;'>Formulario enviado correctamente!</span>";
        }
    });

    // Función para validar el nombre.
    function validateNombre() {
        const value = nombres.value.trim();
        if (value === "") {
            showError("El campo Nombre no puede estar vacío.");
            return false;
        }
        return true;
    }

    // Función que valida el correo.
    function validateCorreo() {
        const value = correo.value.trim();
        if (value === "") {
            showError("El campo Correo no puede estar vacío.");
            return false;
        } else if (!validateEmail(value)) {
            showError("El formato del correo es inválido.");
            return false;
        }
        return true;
    }

    // Función que valida la dirección.
    function validateDireccion() {
        const value = direccion.value.trim();
        if (value === "") {
            showError("El campo Dirección no puede estar vacío.");
            return false;
        }
        return true;
    }

    // Función que valida la cantidad de residuos.
    function validateCantidad() {
        const value = cantidadRes.value.trim();
        if (value === "" || parseInt(value) < 1) {
            showError("Debe ingresar una cantidad válida de residuos.");
            return false;
        }
        return true;
    }

    // Función que valida el tipo de residuo.
    function validateMaterial() {
        const value = material.value;
        if (value === "") {
            showError("Debe seleccionar un tipo de residuo.");
            return false;
        }
        return true;
    }

    // Función que muestra el mensaje de error.
    function showError(message) {
        errorDiv.innerHTML = message;
    }

    // Función que valida el formato de correo.
    function validateEmail(email) {
        const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return re.test(email);
    }
});