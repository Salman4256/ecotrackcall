'use strict';
/**
 * Vercel Serverless Function entrypoint for EcoTrack Express API.
 * Forwards all /api/* requests directly to the Express application.
 */
const app = require('../backend/src/server');

module.exports = app;
