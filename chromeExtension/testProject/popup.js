document.addEventListener('DOMContentLoaded', () => {
    const actionButton = document.getElementById('testButton')
  
    actionButton.addEventListener('click', () => {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'performAction' })
      })
    })
  })