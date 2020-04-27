Cypress.Commands.add(
    'dropFile', {
        prevSubject: false
    }, (fileName) => {
        Cypress.log({
            name: 'dropFile',
        })
        return cy
            .fixture(fileName, 'base64')
            .then(Cypress.Blob.base64StringToBlob)
            .then(blob => {
                // instantiate File from `application` window, not cypress window
                return cy.window().then(win => {
                    const file = new win.File([blob], fileName)
                    const dataTransfer = new win.DataTransfer()
                    dataTransfer.items.add(file)

                    return cy.document().trigger('drop', {
                        dataTransfer,
                    })
                })
            })
    }
)
