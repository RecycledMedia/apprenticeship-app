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