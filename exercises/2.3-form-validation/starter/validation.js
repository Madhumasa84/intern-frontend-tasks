// Exercise 2.3: Form with Validation

// TODO 1: select the form and the toast
// const form = document.getElementById("recordForm");
// const toast = document.getElementById("toast");

// TODO 2: todayISO() -> "YYYY-MM-DD" in the user's LOCAL time zone (see the guide's date trap)
//         then set the min attribute of #apptDate to todayISO() on load.

// TODO 3: validators: one function per field returning "" when valid or an error message.
// const validators = {
//   contactName: (value) => ...,
//   phone: (value) => ...,      // ignore spaces and dashes, then require exactly 10 digits
//   apptDate: (value) => ...,   // required and not in the past (compare strings)
//   apptTime: (value) => ...,
//   notes: (value) => ...,      // optional, max 200 characters
// };

// TODO 4: validateField(name) -> reads the input, runs the validator, then
//         - writes the message into #<name>-error
//         - toggles the "invalid" class and aria-invalid
//         - returns true when valid

// TODO 5: validateForm() -> validate all fields, focus the FIRST invalid one, return true or false

// TODO 6: events
//   - form "submit": preventDefault, validateForm(), if valid -> showToast(...) and form.reset()
//   - each input "blur": validateField
//   - each input "input": re-validate only if the field already shows an error
//   - notes "input": update the "0 / 200" counter

// TODO 7: showToast(message) -> set textContent (NOT innerHTML), unhide, hide after ~3000 ms
