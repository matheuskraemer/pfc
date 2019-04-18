/*
 * Copyright (C) 2011 Google Inc.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */

package org.ros.android.view;

import android.content.Context;
import android.util.AttributeSet;
import android.widget.TextView;
import org.ros.android.MessageCallable;
import org.ros.message.MessageListener;
import org.ros.namespace.GraphName;
import org.ros.node.ConnectedNode;
import org.ros.node.Node;
import org.ros.node.NodeMain;
import org.ros.node.topic.Publisher;
import org.ros.node.topic.Subscriber;

import java.util.Timer;
import java.util.TimerTask;

import sensor_msgs.NavSatFix;


/**
 * @author damonkohler@google.com (Damon Kohler)
 */
public class RosTextView<T> extends TextView implements NodeMain {

  private String topicName;
  private String messageType;
  private MessageCallable<String, T> callable;
  private MessageCallable<String, geometry_msgs.PoseWithCovariance> callablePoint;
  private std_msgs.String pubMessage;
  private geometry_msgs.PoseWithCovariance pubWaypoint;
  private Publisher<std_msgs.String> publisher;
  private Publisher<geometry_msgs.PoseWithCovariance> publisherWaypoint;
  private Timer publisherTimer;
  private Timer publisherWayPointTimer;
  public volatile boolean publish;



  public RosTextView(Context context) {
    super(context);
  }

  public RosTextView(Context context, AttributeSet attrs) {
    super(context, attrs);
  }

  public RosTextView(Context context, AttributeSet attrs, int defStyle) {
    super(context, attrs, defStyle);
  }

  public void setTopicName(String topicName) {
    this.topicName = topicName;
  }


  public void setPublishMessage(String message) {
    this.pubMessage.setData(message);
  }

    public void setPublishWaypoint(Double latitude, Double longitude, Float altura, Double roll, Double pitch, Double yaw, Integer heading_direction) {
        this.pubWaypoint.getPose().getPosition().setX(latitude);
        this.pubWaypoint.getPose().getPosition().setY(longitude);
        this.pubWaypoint.getPose().getPosition().setZ(altura);
        this.pubWaypoint.getPose().getOrientation().setX(roll);
        this.pubWaypoint.getPose().getOrientation().setY(pitch);
        this.pubWaypoint.getPose().getOrientation().setZ(yaw);
        this.pubWaypoint.getPose().getOrientation().setW(heading_direction);
    }

  public void setMessageType(String messageType) {
    this.messageType = messageType;
  }

  public void setMessageToStringCallable(MessageCallable<String, T> callable) {
    this.callable = callable;
  }

    public void setMessageToStringCallablePoint(MessageCallable<String, geometry_msgs.PoseWithCovariance> callable) {
        this.callablePoint = callable;
    }

  @Override
  public GraphName getDefaultNodeName() {
    return GraphName.of("android_gingerbread/ros_text_view");
  }

  @Override
  public void onStart(ConnectedNode connectedNode) {
    this.publish = true;

    //publicador de estado
    publisher = connectedNode.newPublisher("dji/status", std_msgs.String._TYPE);
    pubMessage = publisher.newMessage();
    publisherTimer = new Timer();
    publisherTimer.schedule(new TimerTask() {
      @Override
      public void run() {

          if (!publish)
          {
              pubMessage.setData("");
              publish = true;
              
          }

        if (!pubMessage.getData().equals(""))
        {
            publisher.publish(pubMessage);
            //pubMessage.setData("");
            publish = false;
        }




      }
    }, 0, 50);

        //publicador de ponto atual
      publisherWaypoint = connectedNode.newPublisher("dji/current_pose", geometry_msgs.PoseWithCovariance._TYPE);
      pubWaypoint = publisherWaypoint.newMessage();
      publisherWayPointTimer = new Timer();
      publisherWayPointTimer.schedule(new TimerTask() {
      @Override
      public void run() {
          if (publish) {
              publisherWaypoint.publish(pubWaypoint);
          }
      }
  }, 0, 100);


    //subescreve comandos
    Subscriber<T> subscriber = connectedNode.newSubscriber("dji/command", std_msgs.String._TYPE);
    subscriber.addMessageListener(new MessageListener<T>() {
      @Override
      public void onNewMessage(final T message) {
        if (callable != null) {
          post(new Runnable() {
            @Override
            public void run() {
              setText(callable.call(message));
            }
          });
        } else {
          post(new Runnable() {
            @Override
            public void run() {
              setText(message.toString());
            }
          });
        }
        postInvalidate();
      }
    });

        //subscreve novos waypoints
  Subscriber<geometry_msgs.PoseWithCovariance> subscriberPoint = connectedNode.newSubscriber("dji/waypoint", geometry_msgs.PoseWithCovariance._TYPE);
  subscriberPoint.addMessageListener(new MessageListener<geometry_msgs.PoseWithCovariance>() {
      @Override
      public void onNewMessage(final geometry_msgs.PoseWithCovariance message) {
          if (callablePoint != null) {
              post(new Runnable() {
                  @Override
                  public void run() {
                      callablePoint.call(message);
                  }
              });
          } else {
              post(new Runnable() {
                  @Override
                  public void run() {
                      //setText(message.toString());
                  }
              });
          }
          postInvalidate();
      }
  });
  }

  @Override
  public void onShutdown(Node node) {
  }

  @Override
  public void onShutdownComplete(Node node) {
  }

  @Override
  public void onError(Node node, Throwable throwable) {
  }
}