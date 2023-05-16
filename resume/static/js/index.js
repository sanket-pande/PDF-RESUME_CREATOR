let printArea = document.getElementById("resume-container")

printfunction = () => {
    resumeIframe = printArea.contentWindow;
    resumeIframe.focus()
    resumeIframe.print()
}

document.getElementById("print-resume-btn").addEventListener("click", printfunction)