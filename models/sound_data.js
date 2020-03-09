const mongoose = require('mongoose')

const SoundDataSchema = mongoose.Schema({
    data_id: mongoose.Schema.Types.ObjectId,
    audio: String,
    envelope: String,
    gate: String,
    timestamp: String
})

module.exports = mongoose.model('SoundData', SoundDataSchema)