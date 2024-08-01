const searchButtonContainerIds = [
    "search-bar-entry",
    "search-bar-entry-mobile",
];

// Clone and replace, needed to remove existing event listeners
const clonedSearchButtonContainers = searchButtonContainerIds.map((id) => {
    const originalElement = document.getElementById(id);
    const clonedElement = originalElement.cloneNode(true);
    originalElement.parentNode.replaceChild(clonedElement, originalElement);
  
    return clonedElement;
});

clonedSearchButtonContainers.forEach((trigger) => {
    trigger.addEventListener("click", function () {
        window.alert('Search bar')
    });
});

window.addEventListener(
    "keydown",
    (event) => {
        if (
        (event.metaKey || event.ctrlKey) &&
        (event.key === "k" || event.key === "K")
        ) {
            event.stopPropagation();
            window.alert('Search bar')
            return false;
        }
    },
    true
);