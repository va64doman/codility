import { Component, Injectable } from '@angular/core';

@Component({
    selector: 'like-button',
    templateUrl: './angularLikeButton.component.html',
    styleUrls: ['./angularLikeButton.component.css']
})

export class ButtonComponent {
  likeCount= 100;
  isLiked = false;
  
  likeTheButton = () => {
    if(this.isLiked)
    this.likeCount--;
    else
    this.likeCount++;

    this.isLiked = !this.isLiked
  }
}