---
title: "Find Scholarships"
date: 2024-05-18T00:00:00
draft: false
---

<h1>Find Scholarships</h1>

<form id="search-form">
    <input type="text" id="query" placeholder="Search by name or university">
    <select id="type">
        <option value="">Type of Scholarship</option>
        <option value="Need Based">Need Based</option>
        <option value="Merit Based">Merit Based</option>
        <option value="Need Blind">Need Blind</option>
    </select>
    <select id="coverage">
        <option value="">Coverage</option>
        <option value="Full Ride">Full Ride</option>
        <option value="Full Tuition">Full Tuition</option>
        <option value="Partial Scholarships">Partial Scholarships</option>
    </select>
    <button type="submit">Search</button>
</form>

<div id="results"></div>

<script src="/js/search.js"></script>
