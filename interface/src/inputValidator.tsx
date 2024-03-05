export function setupInputValidation() {
    const inputElement = document.getElementById('search-article') as HTMLInputElement;
    if (inputElement) {
        inputElement.addEventListener('input', () => {
            const value = parseInt(inputElement.value);
            if (isNaN(value) || value < 1 || value > 10) {
                inputElement.value = '';
            }
        });
    } else {
        console.error('Element with ID "search-article" not found');
    }
}