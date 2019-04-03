; Auto-generated. Do not edit!


(cl:in-package quad_planning-msg)


;//! \htmlinclude DJIanswer.msg.html

(cl:defclass <DJIanswer> (roslisp-msg-protocol:ros-message)
  ((position_reached
    :reader position_reached
    :initarg :position_reached
    :type cl:integer
    :initform 0)
   (image_processing_result
    :reader image_processing_result
    :initarg :image_processing_result
    :type cl:integer
    :initform 0))
)

(cl:defclass DJIanswer (<DJIanswer>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DJIanswer>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DJIanswer)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name quad_planning-msg:<DJIanswer> is deprecated: use quad_planning-msg:DJIanswer instead.")))

(cl:ensure-generic-function 'position_reached-val :lambda-list '(m))
(cl:defmethod position_reached-val ((m <DJIanswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader quad_planning-msg:position_reached-val is deprecated.  Use quad_planning-msg:position_reached instead.")
  (position_reached m))

(cl:ensure-generic-function 'image_processing_result-val :lambda-list '(m))
(cl:defmethod image_processing_result-val ((m <DJIanswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader quad_planning-msg:image_processing_result-val is deprecated.  Use quad_planning-msg:image_processing_result instead.")
  (image_processing_result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DJIanswer>) ostream)
  "Serializes a message object of type '<DJIanswer>"
  (cl:let* ((signed (cl:slot-value msg 'position_reached)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'image_processing_result)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DJIanswer>) istream)
  "Deserializes a message object of type '<DJIanswer>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'position_reached) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'image_processing_result) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DJIanswer>)))
  "Returns string type for a message object of type '<DJIanswer>"
  "quad_planning/DJIanswer")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DJIanswer)))
  "Returns string type for a message object of type 'DJIanswer"
  "quad_planning/DJIanswer")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DJIanswer>)))
  "Returns md5sum for a message object of type '<DJIanswer>"
  "7c7d7f35308ecd11c127fbb2710e52ba")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DJIanswer)))
  "Returns md5sum for a message object of type 'DJIanswer"
  "7c7d7f35308ecd11c127fbb2710e52ba")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DJIanswer>)))
  "Returns full string definition for message of type '<DJIanswer>"
  (cl:format cl:nil "int32 position_reached~%int32 image_processing_result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DJIanswer)))
  "Returns full string definition for message of type 'DJIanswer"
  (cl:format cl:nil "int32 position_reached~%int32 image_processing_result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DJIanswer>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DJIanswer>))
  "Converts a ROS message object to a list"
  (cl:list 'DJIanswer
    (cl:cons ':position_reached (position_reached msg))
    (cl:cons ':image_processing_result (image_processing_result msg))
))
