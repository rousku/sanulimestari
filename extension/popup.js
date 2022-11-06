window.addEventListener('DOMContentLoaded', (loadedEvent) => {
    const importButton = document.getElementById('importButton')
    importButton.addEventListener('click', (buttonEvent) => {
        var file = document.getElementById("wordListFile").files[0];
        var statusElement = document.getElementById("status")

        statusElement.innerHTML = ''
        if (file) {
            var reader = new FileReader();
            reader.readAsText(file, "UTF-8");
            reader.onload = function (readerEvent) {
                const wordList = JSON.parse(readerEvent.target.result)
                chrome.storage.local.set(wordList)
                statusElement.innerHTML = "OK";
            }
            reader.onerror = function (readerEvent) {
                statusElement.innerHTML = "Tiedoston luku epäonnistui!";
            }
        }
    })
});