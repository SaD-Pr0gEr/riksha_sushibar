(function () {
    document.addEventListener('click', modalHandler);

    function modalHandler(evt) {
        const modalBtnOpen = evt.target.closest('.js-modal');
        if (modalBtnOpen) { // open btn click
            const modalSelector = modalBtnOpen.dataset.modal;
            showModal(document.querySelector(modalSelector));
        }

        const modalBtnClose = evt.target.closest('.modal-close');
        if (modalBtnClose) { // close btn click
            evt.preventDefault();
            hideModal(modalBtnClose.closest('.modal-window'));
        }

        if (evt.target.matches('#modal-backdrop')) { // backdrop click
            hideModal(document.querySelector('.modal-window.show'));
        }
    }

    function showModal(modalElem) {
        modalElem.classList.add('show');
    }

    function hideModal(modalElem) {
        modalElem.classList.remove('show');
    }
})();
