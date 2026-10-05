// Exercise 2.2: Dynamic Filter UI
// Goal: filter the table rows live by status AND caller number, with no page reload.

// TODO 1: grab the elements you need
// const statusFilter = document.getElementById("statusFilter");
// const searchInput = document.getElementById("searchInput");
// const resultCount = document.getElementById("resultCount");
// const emptyState = document.getElementById("emptyState");
// const clearButton = document.getElementById("clearFilters");
// const rows = Array.from(document.querySelectorAll("#callsTable tbody tr"));

// TODO 2: normalize(text) -> lowercase and strip everything except letters and digits
//         so "+91 98765-43210" becomes "919876543210"

// TODO 3: applyFilters()
//   - read the selected status and the normalized search text
//   - for each row: show it only if (status is "all" OR row.dataset.status === status)
//                    AND the normalized caller number includes the query
//   - toggle row.hidden
//   - update resultCount text: "Showing X of Y calls"
//   - show or hide emptyState

// TODO 4: addEventListener("change", ...) on the select and ("input", ...) on the search box

// TODO 5: clear button resets both controls and calls applyFilters()

// TODO 6: call applyFilters() once at the end so the count is correct on load
