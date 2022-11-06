function pressButton(text) {
  const regex = new RegExp('^'+text+'$')
  cy.get('button').contains(regex).click()
}

describe('empty spec', () => {
  it('passes', () => {
    cy.visit('https://sanuli.fi')
    cy.get('.title-icon').contains('≡').click()
    cy.get('button').contains('Päivän sanuli').click()
    pressButton('O')
    pressButton('N')
    pressButton('T')
    pressButton('T')
    pressButton('O')
    pressButton('ARVAA')
  })
  it('remembers', () => {
    cy.visit('https://sanuli.fi')
    cy.get('.title-icon').contains('≡').click()
    cy.get('button').contains('Päivän sanuli').click()
  })
})