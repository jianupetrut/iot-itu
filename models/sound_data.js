const mongoose = require('mongoose')

const SoundDataSchema = mongoose.Schema({
    data_id: mongoose.Schema.Types.ObjectId,
    readings: [{
        // timestamp: String,
        // audio: String,
        // envelope: String,
        // gate: String
    }]


})

module.exports = mongoose.model('SoundData', SoundDataSchema)