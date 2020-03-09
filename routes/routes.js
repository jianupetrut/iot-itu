const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const SoundData = require('../models/sound_data');

router.get("/hello", (req, res, next) => {
    return res.status(200).json({
        "message": "hello"
    });
});

router.post("/new_recording", (req, res, next) => {
    const newRecording = new SoundData({
        audio: req.body.payload_fields.audio,
        gate: req.body.payload_fields.gate,
        envelope: req.body.payload_fields.envelope,
        timestamp: req.body.metadata.time
    })

    newRecording
    .save()
    .then(result => {
        return res.status(200).json({result})
    })
    .catch(err => res.status(500).json(err));
})

module.exports = router;