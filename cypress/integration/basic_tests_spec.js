const pageObject = {
    textField: '#tap-form input',
    submitTaskButton: '#tap-form button',
    taskEntries: '#tap-list li',
    markTaskCompleteButton: 'a[aria-label="Mark Task Complete"]',
    deleteTaskButton: 'a[aria-label="Remove Task"]',
    hideCompletedTasksToggle: '#form-toggle-container a',
    completedTasks: 'li.task-complete'
};

describe('User submits a new task', function() {
    it('appears in the task list', function() {
        // Construct test data
        const testTask = `Make sure this task exists. ${Date.now()}`;

        // Actual steps we perform in the browser
        cy.visit('/');
        cy.get(pageObject.textField).type(testTask);
        cy.get(pageObject.submitTaskButton).click();
        cy.contains(pageObject.taskEntries, testTask).should.exist;
    })
})

describe('User deletes a task', function() {
    it('no longer displays in the task list', function() {
        // Construct test data
        const testTask = `Make sure this task exists. ${Date.now()}`;
        // Actual steps we perform in the browser
        cy.visit('/');
        cy.get(pageObject.taskEntries).then(({length: initialLength}) => {
            cy.get(pageObject.textField).type(testTask);
            cy.get(pageObject.submitTaskButton).click();
            verifyEntriesCount(initialLength + 1);
            cy.contains(pageObject.taskEntries, testTask).find(pageObject.deleteTaskButton).click();
            verifyEntriesCount(initialLength);
            cy.get(pageObject.taskEntries).then(entries => {
                Object.values(entries).forEach(entry => {
                    expect(entry.innerText).not.to.eq(testTask);
                })
            })
        })
    })
})

function verifyEntriesCount(expectedAmount) {
    cy.get(pageObject.taskEntries).then(entries => {
        expect(entries.length).to.eq(expectedAmount);
    });
}