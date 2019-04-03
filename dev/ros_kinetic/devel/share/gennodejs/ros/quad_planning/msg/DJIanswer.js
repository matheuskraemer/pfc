// Auto-generated. Do not edit!

// (in-package quad_planning.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class DJIanswer {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.position_reached = null;
      this.image_processing_result = null;
    }
    else {
      if (initObj.hasOwnProperty('position_reached')) {
        this.position_reached = initObj.position_reached
      }
      else {
        this.position_reached = 0;
      }
      if (initObj.hasOwnProperty('image_processing_result')) {
        this.image_processing_result = initObj.image_processing_result
      }
      else {
        this.image_processing_result = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DJIanswer
    // Serialize message field [position_reached]
    bufferOffset = _serializer.int32(obj.position_reached, buffer, bufferOffset);
    // Serialize message field [image_processing_result]
    bufferOffset = _serializer.int32(obj.image_processing_result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DJIanswer
    let len;
    let data = new DJIanswer(null);
    // Deserialize message field [position_reached]
    data.position_reached = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [image_processing_result]
    data.image_processing_result = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'quad_planning/DJIanswer';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7c7d7f35308ecd11c127fbb2710e52ba';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 position_reached
    int32 image_processing_result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DJIanswer(null);
    if (msg.position_reached !== undefined) {
      resolved.position_reached = msg.position_reached;
    }
    else {
      resolved.position_reached = 0
    }

    if (msg.image_processing_result !== undefined) {
      resolved.image_processing_result = msg.image_processing_result;
    }
    else {
      resolved.image_processing_result = 0
    }

    return resolved;
    }
};

module.exports = DJIanswer;
