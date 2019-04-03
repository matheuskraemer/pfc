
(cl:in-package :asdf)

(defsystem "quad_planning-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "DJIanswer" :depends-on ("_package_DJIanswer"))
    (:file "_package_DJIanswer" :depends-on ("_package"))
  ))