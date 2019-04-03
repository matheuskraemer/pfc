;; Auto-generated. Do not edit!


(when (boundp 'quad_planning::DJIanswer)
  (if (not (find-package "QUAD_PLANNING"))
    (make-package "QUAD_PLANNING"))
  (shadow 'DJIanswer (find-package "QUAD_PLANNING")))
(unless (find-package "QUAD_PLANNING::DJIANSWER")
  (make-package "QUAD_PLANNING::DJIANSWER"))

(in-package "ROS")
;;//! \htmlinclude DJIanswer.msg.html


(defclass quad_planning::DJIanswer
  :super ros::object
  :slots (_position_reached _image_processing_result ))

(defmethod quad_planning::DJIanswer
  (:init
   (&key
    ((:position_reached __position_reached) 0)
    ((:image_processing_result __image_processing_result) 0)
    )
   (send-super :init)
   (setq _position_reached (round __position_reached))
   (setq _image_processing_result (round __image_processing_result))
   self)
  (:position_reached
   (&optional __position_reached)
   (if __position_reached (setq _position_reached __position_reached)) _position_reached)
  (:image_processing_result
   (&optional __image_processing_result)
   (if __image_processing_result (setq _image_processing_result __image_processing_result)) _image_processing_result)
  (:serialization-length
   ()
   (+
    ;; int32 _position_reached
    4
    ;; int32 _image_processing_result
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _position_reached
       (write-long _position_reached s)
     ;; int32 _image_processing_result
       (write-long _image_processing_result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _position_reached
     (setq _position_reached (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _image_processing_result
     (setq _image_processing_result (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get quad_planning::DJIanswer :md5sum-) "7c7d7f35308ecd11c127fbb2710e52ba")
(setf (get quad_planning::DJIanswer :datatype-) "quad_planning/DJIanswer")
(setf (get quad_planning::DJIanswer :definition-)
      "int32 position_reached
int32 image_processing_result

")



(provide :quad_planning/DJIanswer "7c7d7f35308ecd11c127fbb2710e52ba")


