

// Funçao da api do chrome ao instalar a extensao ou atualisar
chrome.runtime.onInstalled.addListener(function (object){
    //criar nova aba e entra no site
    chrome.tabs.create({
        url: "https://bloi308.com/sorteios?ref=OdxkK5x8G0Uu12wFOEp3rlY4yh53&tab=sweepstakes0#",
    });
});


chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['content.js']
    });
});
  
