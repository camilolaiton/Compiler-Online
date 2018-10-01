$(document).ready(function() {

    $('#guardar_local').click(function(event) {
        contenido = $('#inputTextToSave').val();

        if(contenido != ""){
            saveTextAsFile();
            swal("Correcto!", "Archivo guardado con exito!", "success");

            /*
            swal({
              type: 'success',
              title: 'Correcto! Archivo guardado con exito',
              padding: '3em',
              backdrop: `
                rgba(0,0,123,0.4)
              `
            })
            */

        }
        else{
            swal("Es necesario un codigo!", "No ha escrito codigo en el espacio 'Codigo fuente'", "warning");

            /*
            swal({
              type: 'warning',
              title: 'Es necesario un codigo!',
              text: "No ha escrito codigo en el espacio 'Codigo fuente'",
              padding: '4em',
              backdrop: `
                rgba(239,0,0,0.8)
              `
            })
            */
        }

        return false
    });

    $.extend(jQuery.expr[":"], 
    {
        "contiene-palabra": function(elem, i, match, array) {
            return (elem.textContent || elem.innerText || jQuery(elem).text() || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
        }
    });
    
    $('#btnCorrer').click(function(event) {
        contenido = $('#inputTextToSave').val();
        $('#resultados').text("")

        if(contenido != ""){
            $.ajax({
                headers: { "X-CSRFToken": getCookie("csrftoken") },
                url: 'enviarCodigo/',
                type: "POST",
                data: {'contenido': contenido, 'nombreCodigo': $('#nombreCodigo').text()},
                success: function (response) {
                   //lo que haces si es exitoso
                   $('#resultados').text(response.resultado)
                }

            });
        }
        else{
            swal("Es necesario un codigo!", "No ha escrito codigo en el espacio 'Codigo fuente'", "warning");
            /*
            swal({
              type: 'warning',
              title: 'Es necesario un codigo!',
              text: "No ha escrito codigo en el espacio 'Codigo fuente'",
              padding: '4em',
              backdrop: `
                rgba(239,0,0,0.8)
              `
            })
            */
        }

        return false

    });

    $('#guardar_nube').click(function(event) {

        contenido = $('#inputTextToSave').val();

        if(contenido != ""){

            swal("Ingrese el nombre de su archivo a guardar:", {
              content: "input",
            })
            .then((value) => {
                if(value == ""){
                    swal('Es necesario un nombre para el archivo');
                }
                else{

                    $.ajax({
                        headers: { "X-CSRFToken": getCookie("csrftoken") },
                        url: 'Codigo/subirCodigo/',
                        type: "POST",
                        data: {'contenido': contenido, "filename":value},
                        success: function (response) {
                           //lo que haces si es exitoso
                           //$('#resultados').text(response.resultado)

                           if(response.mensaje == 1){
                               swal("Correcto!", response.resultado, "success");
                           }
                           else{
                               /*
                               swal({
                                  type: 'error',
                                  title: 'Ha ocurrido un error!',
                                  text: response.resultado,
                                  footer: '<a href>Why do I have this issue?</a>',
                                })
                                */

                               swal("Corrcto!", response.resultado , "success");
                           }
                        }

                    });
                }

            });
        }
        else{
            swal("Es necesario un codigo!", "No ha escrito codigo en el espacio 'Codigo fuente'", "warning");
        }

        return false

    });

    $('#buscar_nube').click(function(event) {

        swal("Ingrese el nombre de su archivo a buscar:", {
          content: "input",
        })
        .then((value) => {
            if(value == ""){
                swal('Es necesario un nombre para la busqueda del archivo');
            }
            else{

                $.ajax({
                    headers: { "X-CSRFToken": getCookie("csrftoken") },
                    url: 'Codigo/buscarCodigo/',
                    type: "POST",
                    data: {"filename":value},
                    success: function (response) {
                       //lo que haces si es exitoso
                       //$('#resultados').text(response.resultado)

                       if(response.mensaje == 1){
                           swal("Correcto!", "El archivo ha sido encontrado", "success");
                           $('#inputTextToSave').text(response.resultado);
                           $('#nombreCodigo').text(value);
                       }
                       else{
                           /*
                           swal({
                              type: 'error',
                              title: 'Ha ocurrido un error!',
                              text: response.resultado,
                              footer: '<a href>Why do I have this issue?</a>',
                            })
                            */

                           swal("Ha ocurrido un error!", response.resultado , "error");
                       }
                    }

                });
            }

        });

        return false

    });

    $('#btn_buscar_texto').click(function(event) {
        buscar = $('#texto_buscar').val();
        contenido = $('#inputTextToSave').val();

        if(contenido != "" && buscar != ""){
            pos = contenido.indexOf(buscar);

            if(pos != -1){
                setCaretToPos(document.getElementById("inputTextToSave"), pos);
            }
            else{
                swal("Opss...", "No ha sido encontrado!", "warning")
            }

        }
        else{
            swal("Opss...", "No hay nada que buscar!", "warning")
        }

        return false

    });

});

$.extend($.expr[":"], 
{
    "contains-ci": function(elem, i, match, array) 
    {
        return (elem.textContent || elem.innerText || $(elem).text() || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
});

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function saveTextAsFile()
{
// grab the content of the form field and place it into a variable
    var textToWrite = document.getElementById("inputTextToSave").value;
//  create a new Blob (html5 magic) that conatins the data from your form feild
    var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
// Specify the name of the file to be saved
    var fileNameToSaveAs = "_codigo.txt";
    
// Optionally allow the user to choose a file name by providing 
// an imput field in the HTML and using the collected data here
// var fileNameToSaveAs = txtFileName.text;
 
// create a link for our script to 'click'
    var downloadLink = document.createElement("a");
//  supply the name of the file (from the var above).
// you could create the name here but using a var
// allows more flexability later.
    downloadLink.download = fileNameToSaveAs;
// provide text for the link. This will be hidden so you
// can actually use anything you want.
    downloadLink.innerHTML = "My Hidden Link";
    
// allow our code to work in webkit & Gecko based browsers
// without the need for a if / else block.
    window.URL = window.URL || window.webkitURL;
          
// Create the link Object.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
// when link is clicked call a function to remove it from
// the DOM in case user wants to save a second file.
    downloadLink.onclick = destroyClickedElement;
// make sure the link is hidden.
    downloadLink.style.display = "none";
// add the link to the DOM
    document.body.appendChild(downloadLink);
    
// click the new link
    downloadLink.click();
}
 
function destroyClickedElement(event)
{
// remove the link from the DOM
    document.body.removeChild(event.target);
}

function setSelectionRange(input, selectionStart, selectionEnd) {
  if (input.setSelectionRange) {
    input.focus();
    input.setSelectionRange(selectionStart, selectionEnd);
  }
  else if (input.createTextRange) {
    var range = input.createTextRange();
    range.collapse(true);
    range.moveEnd('character', selectionEnd);
    range.moveStart('character', selectionStart);
    range.select();
  }
}

function setCaretToPos (input, pos) {
  setSelectionRange(input, pos, pos);
}
 
// EOF