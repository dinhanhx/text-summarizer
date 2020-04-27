import './commands.js'

describe('The Home Page', () => {
  it('successfully loads', () => {
    cy.visit('http://localhost:5000/text-summarizer')
  })
})

describe('Light/Dark mode', () => {
  before(() => {
    cy.visit('http://localhost:5000/text-summarizer')
  })
  specify('switch light to dark', () => {
      cy.contains('dark/light').click()
  })
  specify('switch dark to light', () => {
      cy.contains('dark/light').click()
  })
})

describe('Summarize', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5000/text-summarizer')
  })
  specify('Can summarize text', () => {
      cy.contains('Text here').type('Returning to Hawaii in 1877, he worked as a government tax collector and road supervisor for the island of Kauai, where he settled down. After the annexation of Hawaii to the United States, Bush was recognized for his military service, and in 1905 was granted a government pension for the injuries he received in the')
      cy.get('#text').submit()
  })
  specify('Can summarize Wiki', () => {
      cy.contains('Wikipedia url here').type('https://en.wikipedia.org/wiki/James_Wood_Bush')
      cy.get('#wiki').submit()
  })
  specify('Can summarize file', () => {
   	 cy.get('#file').trigger('dragenter')
   	 cy.dropFile('sample1.pdf')
         cy.get('#file').submit()
  });
})

