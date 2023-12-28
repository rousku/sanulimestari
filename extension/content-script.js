const observer = new MutationObserver(mutations => {

    document.querySelectorAll('.tile:not(.current)').forEach(elem => {
        elem.style.removeProperty('background-color')
    })

    if (document.querySelector('h1.title')?.innerText.includes('PÄIVÄN SANULI')) {

        currentWord = Array.from(document.querySelectorAll('.tile.current')).map(tile => tile.innerText).join('')

        document.querySelectorAll('.tile.current').forEach(elem => {

            chrome.storage.local.get(currentWord, results => {
                if (currentWord in results) {
                    elem.style.setProperty('background-color', 'red')
                }
                else {
                    elem.style.removeProperty('background-color')
                }
            })
            
        })

        const solvedSanuliTiles = document.querySelectorAll('.row-5:not(:has(.present)):not(:has(.absent)):not(:has(.current)):has(.correct) > .tile')
        const solvedSanuliOfTheDay = Array.from(solvedSanuliTiles).map(tile => tile.innerText).join('')
        const unSolvedSanuliOfheDay = document.querySelector('.message')?.textContent?.match(/Sana oli "([\wÖÄ]+)"/)?.[1]

        const sanuliOfTheDay = solvedSanuliOfTheDay ? solvedSanuliOfTheDay : unSolvedSanuliOfheDay
        if (sanuliOfTheDay) {
            var obj = {}
            obj[sanuliOfTheDay] = true
            chrome.storage.local.set(obj)

            solvedSanuliTiles.forEach(elem => {
                elem.style.setProperty('border', '5px darkgreen solid')
            })
        }
        
    }
});

observer.observe(document.body, {
    attributes: true,
    characterData: true,
    subtree: true
});