const botao = document.getElementById("btn")
const numero = document.getElementById("Numero")
const parar = document.getElementById("btn_stop")
const sav_edit = document.getElementById("sav_edit")
const contener = document.getElementById('container')


var maquina = true
var modo = true


setInterval(() => {
  chrome.storage.local.get(['Numero'], function(result){
    
    numero.value = result

    console.log("resgatando o valor armazendado")
  })
}, 1000);



botao.addEventListener('click', async () => {
  // ocultar botoes e aparecer funcoes
  botao.style.display = "none";
  parar.style.display = "inline"
  //__________________________________\\

  // Envia uma mensagem para o content.js
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

    chrome.tabs.sendMessage(tabs[0].id, {mensagem: "Iniciar"}, function(response) {
      
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ['content.js']
      });

      console.log("Bot iniciado:", response.resposta);
      
    });
  });
});


parar.addEventListener('click', async () => {
  // ocultar botoes e aparecer funcoes
  botao.style.display = "inline";
  parar.style.display = "none"
  //__________________________________\\
  
  // Envia uma mensagem para o content.js
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

    chrome.tabs.sendMessage(tabs[0].id, {mensagem: "Parar"}, function(response) {
  
        chrome.scripting.executeScript({
          target: { tabId: tab.id },
          files: ['content.js']
        });

        console.log("Bot iniciado:", response.resposta);

     
    });
  });



  

 
});

sav_edit.addEventListener('click', async () => {
  let n = sav_edit.innerText;

  // Salvar valor
  if (n == 'Salvar'){
    sav_edit.innerText = "Editar";
    sav_edit.style.backgroundColor = `rgb(238, 241, 6)`;
    numero.disabled = true;
    
    //armazena valor do numero localmente
    chrome.storage.local.set({'Numero': `${numero.value}`}, function(){
        console.log('Valor armazendado com sucesso!')

    })
    

  // Editar valor
  }else if (n == 'Editar'){
    sav_edit.innerText = "Salvar";
    sav_edit.style.backgroundColor = `rgb(20, 226, 175)`;

    numero.disabled = false;

  }



})

