import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WordsmithComponent } from './wordsmith.component';

describe('WordsmithComponent', () => {
  let component: WordsmithComponent;
  let fixture: ComponentFixture<WordsmithComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WordsmithComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WordsmithComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
