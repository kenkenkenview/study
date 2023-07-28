chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'performAction') {
      // ここに拡張機能の動作を実装する
      alert('Hello, World!');
      console.log('test cleared');
    }
  })