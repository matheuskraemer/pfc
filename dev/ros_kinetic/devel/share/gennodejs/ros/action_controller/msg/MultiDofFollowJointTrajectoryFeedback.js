// Auto-generated. Do not edit!

// (in-package action_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let trajectory_msgs = _finder('trajectory_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class MultiDofFollowJointTrajectoryFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.joint_names = null;
      this.desired = null;
      this.actual = null;
      this.error = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('joint_names')) {
        this.joint_names = initObj.joint_names
      }
      else {
        this.joint_names = [];
      }
      if (initObj.hasOwnProperty('desired')) {
        this.desired = initObj.desired
      }
      else {
        this.desired = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint();
      }
      if (initObj.hasOwnProperty('actual')) {
        this.actual = initObj.actual
      }
      else {
        this.actual = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint();
      }
      if (initObj.hasOwnProperty('error')) {
        this.error = initObj.error
      }
      else {
        this.error = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MultiDofFollowJointTrajectoryFeedback
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [joint_names]
    bufferOffset = _arraySerializer.string(obj.joint_names, buffer, bufferOffset, null);
    // Serialize message field [desired]
    bufferOffset = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.serialize(obj.desired, buffer, bufferOffset);
    // Serialize message field [actual]
    bufferOffset = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.serialize(obj.actual, buffer, bufferOffset);
    // Serialize message field [error]
    bufferOffset = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.serialize(obj.error, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MultiDofFollowJointTrajectoryFeedback
    let len;
    let data = new MultiDofFollowJointTrajectoryFeedback(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [joint_names]
    data.joint_names = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [desired]
    data.desired = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.deserialize(buffer, bufferOffset);
    // Deserialize message field [actual]
    data.actual = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.deserialize(buffer, bufferOffset);
    // Deserialize message field [error]
    data.error = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.joint_names.forEach((val) => {
      length += 4 + val.length;
    });
    length += trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.getMessageSize(object.desired);
    length += trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.getMessageSize(object.actual);
    length += trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.getMessageSize(object.error);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'action_controller/MultiDofFollowJointTrajectoryFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8c3426246094babe60db855c2a9503c7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    Header header
    string[] joint_names
    trajectory_msgs/MultiDOFJointTrajectoryPoint desired
    trajectory_msgs/MultiDOFJointTrajectoryPoint actual
    trajectory_msgs/MultiDOFJointTrajectoryPoint error
    
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint
    # Each multi-dof joint can specify a transform (up to 6 DOF)
    geometry_msgs/Transform[] transforms
    
    # There can be a velocity specified for the origin of the joint 
    geometry_msgs/Twist[] velocities
    
    # There can be an acceleration specified for the origin of the joint 
    geometry_msgs/Twist[] accelerations
    
    duration time_from_start
    
    ================================================================================
    MSG: geometry_msgs/Transform
    # This represents the transform between two coordinate frames in free space.
    
    Vector3 translation
    Quaternion rotation
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: geometry_msgs/Twist
    # This expresses velocity in free space broken into its linear and angular parts.
    Vector3  linear
    Vector3  angular
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MultiDofFollowJointTrajectoryFeedback(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.joint_names !== undefined) {
      resolved.joint_names = msg.joint_names;
    }
    else {
      resolved.joint_names = []
    }

    if (msg.desired !== undefined) {
      resolved.desired = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.Resolve(msg.desired)
    }
    else {
      resolved.desired = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
    }

    if (msg.actual !== undefined) {
      resolved.actual = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.Resolve(msg.actual)
    }
    else {
      resolved.actual = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
    }

    if (msg.error !== undefined) {
      resolved.error = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint.Resolve(msg.error)
    }
    else {
      resolved.error = new trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
    }

    return resolved;
    }
};

module.exports = MultiDofFollowJointTrajectoryFeedback;
